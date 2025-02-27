import string

def palindromes_between_indices(s):
    result = set()
    for i in range(1, 2 + 1):
        for j in range(i + 1, min(i + 3, len(s))):
            substring = s[i:j + 1].lower()
            if all((char in string.ascii_lowercase for char in substring)):
                palindrome = ''.join([substring[0]] + [char for char in substring[::-1] if char != substring[0]])
                if len(palindrome) >= 3:
                    result.add(palindrome)
    return result