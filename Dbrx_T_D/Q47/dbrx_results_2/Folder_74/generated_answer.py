def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(30, 85):
        for j in range(12, 21):
            if i + j - 1 <= len(s) and s[i - 1:i - 1 + j].lower() == s[i - 1:i - 1 + j][::-1].lower():
                result.add(s[i - 1:i - 1 + j])
    return result