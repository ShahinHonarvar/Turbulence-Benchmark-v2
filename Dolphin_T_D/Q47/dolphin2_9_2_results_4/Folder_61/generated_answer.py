def palindromes_of_specific_lengths(s):
    s = s[:30].lower()
    result = set()
    for length in range(20, 31):
        for i in range(len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha():
                result.add(s[i:i + length])
    return result