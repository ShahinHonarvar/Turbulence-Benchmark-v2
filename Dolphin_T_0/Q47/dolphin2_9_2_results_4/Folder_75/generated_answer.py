from string import ascii_lowercase

def palindromes_of_specific_lengths(s):
    s = s[31:75]
    output = set()
    for length in range(23, 40):
        for i in range(len(s)):
            if s[i:i + length] in output or s[i:i + length][::-1] in output:
                continue
            subs = s[i:i + length].lower()
            if all((x in ascii_lowercase for x in subs)) and subs == subs[::-1]:
                output.add(s[i:i + length])
    return output