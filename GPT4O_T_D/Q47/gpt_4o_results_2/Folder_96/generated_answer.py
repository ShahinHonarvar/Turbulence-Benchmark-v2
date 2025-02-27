def palindromes_of_specific_lengths(s):
    s_sub = s[100:301]
    palindromes = set()
    for start in range(len(s_sub)):
        for end in range(start + 50, min(start + 101, len(s_sub) + 1)):
            candidate = s_sub[start:end]
            filtered_candidate = ''.join((c for c in candidate if c.isalpha()))
            if len(filtered_candidate) >= 50:
                if filtered_candidate.lower() == filtered_candidate[::-1].lower():
                    palindromes.add(filtered_candidate)
    return palindromes