def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[124:284]
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                result.add(sub)
    return result