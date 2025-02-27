from string import ascii_lowercase

def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(16, 61):
        for j in range(i + 16):
            for k in range(j + 16):
                substring = s[j:k].lower()
                if substring == substring[::-1] and len(substring) in range(16, 40) and substring.isalpha():
                    result.add(substring)
    return result