def palindromes_of_specific_lengths(S):
    substring = S[105:281]
    result = set()
    for length in range(136, 152):
        for i in range(len(substring)):
            if substring[i:i + length] == substring[i:i + length][::-1] and substring[i:i + length].isalpha():
                result.add(substring[i:i + length].lower())
    return result