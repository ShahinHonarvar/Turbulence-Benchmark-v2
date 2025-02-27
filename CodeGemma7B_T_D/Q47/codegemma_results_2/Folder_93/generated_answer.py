def palindromes_of_specific_lengths(s):
    lowercased_string = s.lower()
    index_range = lowercased_string[16:96]
    final_set = set()
    for i in range(len(index_range)):
        for j in range(i + 12, min(len(index_range), i + 50)):
            substring = index_range[i:j]
            if substring == substring[::-1] and substring.isalpha():
                final_set.add(substring)
    return final_set