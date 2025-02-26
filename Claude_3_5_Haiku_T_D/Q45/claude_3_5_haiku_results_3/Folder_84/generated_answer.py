from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [char for char in s[4:10] if char.isalpha()]
    palindromes = set()

    def generate_palindromes(current_letters):
        if len(current_letters) < 3:
            return
        for perm in set(permutations(current_letters)):
            if len(set(perm)) < 3:
                continue
            for i in range(len(perm)):
                candidate = list(perm)
                mid = len(candidate) // 2
                for j in range(mid):
                    candidate[j], candidate[-(j + 1)] = (candidate[-(j + 1)], candidate[j])
                palindrome = ''.join(candidate)
                if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                    palindromes.add(palindrome)
    generate_palindromes(letters)
    return palindromes