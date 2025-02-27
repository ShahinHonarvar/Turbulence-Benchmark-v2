def palindromes_of_specific_lengths(s):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    sub = s[1:300]
    for start in range(len(sub)):
        for length in range(3, 11):
            if start + length <= len(sub):
                substr = sub[start:start + length]
                filtered_substr = ''.join(filter(lambda c: c in valid_chars, substr))
                if filtered_substr.lower() == filtered_substr[::-1].lower() and len(filtered_substr) == length:
                    palindromes.add(filtered_substr)
    return palindromes