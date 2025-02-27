def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(119, 257):
        for j in range(104, 124):
            if s[i:i + j].lower() == s[i:i + j].lower()[::-1] and s[i:i + j].isalpha():
                result.add(s[i:i + j])
    return result