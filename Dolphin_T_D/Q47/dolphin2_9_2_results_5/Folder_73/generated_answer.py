def palindromes_of_specific_lengths(s):
    s = s[20:63]
    result = set()
    for i in range(len(s) - 21):
        for length in range(22, 34):
            sub = s[i:i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                result.add(sub)
    return result