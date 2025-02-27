def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 98):
        subs = s[i:i + 99]
        subs = ''.join((ch.lower() for ch in subs if ch.isalpha()))
        if subs == subs[::-1]:
            result.add(subs)
    return result