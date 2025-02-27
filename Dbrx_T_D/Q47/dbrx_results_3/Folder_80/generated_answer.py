def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(35, 89):
        for j in range(24, 34):
            if i + j - 1 <= 88 and s[i:i + j].lower() == s[i:i + j][::-1].lower():
                result.add(s[i:i + j])
    return result