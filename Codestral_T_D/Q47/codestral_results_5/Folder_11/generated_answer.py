def palindromes_of_specific_lengths(s):
    s = s[24:98].lower()
    result = set()
    for length in range(10, 37):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result