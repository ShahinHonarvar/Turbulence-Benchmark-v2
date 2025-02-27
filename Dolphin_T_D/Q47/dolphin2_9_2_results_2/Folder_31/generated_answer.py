def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(11, 84):
        for length in range(37, 61):
            if s[i:i + length].lower() == s[i:i + length][::-1].lower():
                result.add(s[i:i + length])
    return result