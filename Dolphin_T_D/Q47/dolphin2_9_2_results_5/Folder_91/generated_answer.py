def palindromes_of_specific_lengths(s):
    subs = s[:11]
    pals = set()
    for length in range(3, 6):
        for i in range(len(subs) - length + 1):
            subs_i = subs[i:i + length]
            if subs_i == subs_i[::-1] and subs_i.isalpha():
                pals.add(subs_i.lower())
    return pals