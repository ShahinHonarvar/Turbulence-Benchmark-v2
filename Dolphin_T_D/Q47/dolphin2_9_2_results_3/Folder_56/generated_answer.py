def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(1, 10):
        for j in range(3, 8):
            if s[i:i + j].lower() == s[i:i + j][::-1].lower():
                result.add(s[i:i + j])
    return result