from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(used_letters):
        if len(used_letters) >= 7:
            if len(set(used_letters)) == len(used_letters):
                for perm in permutations(used_letters):
                    candidate = ''.join(perm)
                    if candidate == candidate[::-1]:
                        palindromes.add(candidate)
        for letter in letters:
            if letters.count(letter) > used_letters.count(letter):
                generate_palindromes(used_letters + [letter])
    generate_palindromes([])
    return palindromes