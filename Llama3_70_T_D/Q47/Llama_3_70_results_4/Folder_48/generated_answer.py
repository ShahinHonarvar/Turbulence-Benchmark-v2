def palindromes_of_specific_lengths(s):
    result = set()
    s = s.upper()
    substring = s[155:284]
    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result