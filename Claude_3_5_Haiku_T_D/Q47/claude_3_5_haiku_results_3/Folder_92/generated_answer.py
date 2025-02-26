def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(len(s[:5]) - 2):
        for j in range(i + 3, i + 5):
            substring = s[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result