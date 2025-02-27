def palindromes_of_specific_lengths(s):
    s = s[16:78]
    result = set()
    for length in range(43, 48):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            letters_only_sub = ''.join(filter(str.isalpha, sub)).lower()
            if letters_only_sub == letters_only_sub[::-1] and len(letters_only_sub) == length:
                result.add(sub)
    return result