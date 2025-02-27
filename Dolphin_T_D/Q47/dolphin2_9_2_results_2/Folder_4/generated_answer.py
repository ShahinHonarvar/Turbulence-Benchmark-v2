def palindromes_of_specific_lengths(s):
    s = s[11:92]
    result = set()
    for length in range(17, 67):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if all((c.isalpha() for c in sub)) and sub.lower() == sub[::-1].lower():
                result.add(sub)
    return result