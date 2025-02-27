def palindromes_of_specific_lengths(s):
    subs = s[155:284]
    result = set()
    for length in range(104, 121):
        for i in range(len(subs) - length + 1):
            subs_of_new_length = subs[i:i + length]
            if subs_of_new_length.lower() == subs_of_new_length[::-1].lower():
                result.add(subs_of_new_length)
    return result