def palindromes_of_specific_lengths(s):
    subs = ''.join((c.lower() for c in s[0:5] if c.isalpha()))
    length_three = {subs[i:i + 3] for i in range(len(subs) - 2) if subs[i:i + 3] == subs[i:i + 3][::-1]}
    length_four = {subs[i:i + 4] for i in range(len(subs) - 3) if subs[i:i + 4] == subs[i:i + 4][::-1]}
    return length_three | length_four