def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    result = set()
    for i in range(3, 5):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                result.add(s[j:j + i])
    return result