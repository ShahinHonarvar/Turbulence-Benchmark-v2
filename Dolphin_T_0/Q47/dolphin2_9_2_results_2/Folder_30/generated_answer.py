def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[14:91]
    result = set()
    for length in range(55, 72):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((c.lower() in english_letters for c in sub)) and sub == sub[::-1]:
                result.add(sub)
    return result