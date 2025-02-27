def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[2:9]
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            letters_only = ''.join(filter(str.isalpha, sub.lower()))
            if letters_only == letters_only[::-1] and 3 <= len(letters_only) <= 4:
                result.add(sub)
    return result