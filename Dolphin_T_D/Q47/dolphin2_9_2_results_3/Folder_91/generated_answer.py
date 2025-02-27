def palindromes_of_specific_lengths(s):
    s = s[:11]
    output = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s)):
            subs = s[i:j + 1].lower()
            if subs == subs[::-1] and 3 <= len(subs) <= 5:
                if subs.isalpha():
                    output.add(subs)
    return output