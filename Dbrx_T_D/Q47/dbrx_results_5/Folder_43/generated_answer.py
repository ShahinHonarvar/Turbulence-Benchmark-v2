def palindromes_of_specific_lengths(s):
    s = s.lower()
    target_indices = s[41:90]
    palindromes = set()
    for i in range(len(target_indices) - 22):
        for j in range(23, 39):
            if i + j <= len(target_indices):
                candidate = target_indices[i:i + j]
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes