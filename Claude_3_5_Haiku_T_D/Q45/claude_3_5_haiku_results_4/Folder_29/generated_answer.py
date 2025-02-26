from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [char for char in s[2:10] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current_letters, start_length):
        for length in range(start_length, len(current_letters) + 1):
            for perm in set(permutations(current_letters, length)):
                if len(set(perm)) >= length // 2:
                    palindrome = ''.join(perm)
                    if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    generate_palindromes(letters, 6)
    return palindromes