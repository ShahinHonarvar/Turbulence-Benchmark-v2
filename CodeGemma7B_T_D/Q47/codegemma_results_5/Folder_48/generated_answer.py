def palindromes_of_specific_lengths(string):
    plendromes_set = set()
    a_to_z = set((chr(ascii_lowercase) for ascii_lowercase in range(ord('a'), ord('z') + 1)))
    for string_index in range(155, 284):
        for palindrome_len in range(104, 121):
            string_slice = string[string_index:string_index + palindrome_len]
            if len(string_slice) < palindrome_len:
                continue
            string_slice_lower = string_slice.lower()
            if set(string_slice_lower).issubset(a_to_z):
                plendromes_set.add(string_slice)
    return plendromes_set