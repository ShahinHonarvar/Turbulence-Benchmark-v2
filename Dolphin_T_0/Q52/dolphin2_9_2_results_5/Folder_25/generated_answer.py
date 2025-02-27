import itertools

def palindrome_of_length_n(s):
    s = s.lower()
    all_subs = set((''.join(sub) for i in range(len(s)) for j in range(i + 90, len(s) + 1) for sub in itertools.combinations(s[i:j], 90)))
    return set((sub for sub in all_subs if sub == sub[::-1] and sub.isalpha()))