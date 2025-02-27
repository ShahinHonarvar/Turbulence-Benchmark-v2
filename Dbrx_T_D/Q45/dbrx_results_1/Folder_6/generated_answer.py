from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_s = s[:8]
    palindromes = set()
    for start in range(8):
        for end in range(start, 8):
            if sub_s[start:end + 1] and set(sub_s[start:end + 1]) <= eng_letters:
                sub_sub_s = sub_s[start:end + 1]
                if len(sub_sub_s) >= 4 and sub_sub_s == sub_sub_s[::-1]:
                    palindromes.add(sub_sub_s)
    return palindromes