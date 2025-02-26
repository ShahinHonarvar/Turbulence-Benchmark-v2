from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:7])).lower()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        if len(chars) <= 2:
            return set()
        result = set()
        for i in range(len(chars)):
            for j in range(i + 2, len(chars)):
                substring = chars[i:j + 1]
                if is_palindrome(substring) and len(substring) >= 3:
                    result.add(substring)
        return result
    palindromes = generate_palindromes(letters)
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes