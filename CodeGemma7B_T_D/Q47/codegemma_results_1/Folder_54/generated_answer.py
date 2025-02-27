def palindromes_of_specific_lengths(str):
    result = set()
    for i in range(27, 78):
        for j in range(i - 18, i + 1):
            str_slice = str[j:i + 1]
            str_slice_lower = str_slice.lower()
            if str_slice_lower == str_slice_lower[::-1] and str_slice.isalpha():
                result.add(str_slice)
    return result