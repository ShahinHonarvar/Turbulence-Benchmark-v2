def palindromes_of_specific_lengths(s):
    starting_index = 63
    ending_index = 70
    s = s[starting_index:ending_index + 1]
    s = ''.join((c for c in s if c.isalpha()))
    lengths = [4, 5]
    pals = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                pals.add(sub.lower())
    return pals