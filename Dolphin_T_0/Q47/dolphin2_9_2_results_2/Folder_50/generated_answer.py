def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(10, 36):
        for i in range(36, 93):
            if i + length <= 93 and s[i:i + length].lower() == s[i:i + length].lower()[::-1] and s[i:i + length].isalpha():
                result.add(s[i:i + length])
    return result