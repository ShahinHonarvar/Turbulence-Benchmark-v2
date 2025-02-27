def palindromes_between_indices(s):
    palindromes = set()
    for i in range(3, 8):
        if i < len(s):
            for j in range(i + 2, len(s) + 1):
                substring = s[i:j]
                if len(substring) >= 6:
                    for palindrome in get_palindromes(substring.lower()):
                        palindromes.add(palindrome)
    return palindromes

def get_palindromes(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result