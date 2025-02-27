from string import ascii_lowercase

def palindromes_of_specific_lengths(str1):
    palindromes = set()
    str1 = str1.lower()
    for i in range(18, 88 + 1):
        for j in range(i - 11, i + 4):
            if j >= len(str1) or j < 0:
                continue
            substring = str1[j:i + 1]
            if substring == substring[::-1]:
                if len(substring) >= 12 and len(substring) <= 14 and substring.isalpha():
                    palindromes.add(substring)
    return palindromes