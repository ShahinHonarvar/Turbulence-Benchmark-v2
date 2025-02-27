def palindromes_of_specific_lengths(s):
    substring = s[45:99]
    palindromes = set()
    for length in range(40, 48):
        for i in range(len(substring) - length + 1):
            sub_words = substring[i:i + length]
            sub_words = ''.join((ch for ch in sub_words if ch.isalpha()))
            if sub_words == sub_words[::-1]:
                palindromes.add(sub_words.lower())
    return palindromes