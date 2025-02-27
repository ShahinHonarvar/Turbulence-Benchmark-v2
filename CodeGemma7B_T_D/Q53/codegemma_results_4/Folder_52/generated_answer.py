def palindrome_of_length_at_least_n(input_str):
    combined_str = input_str.lower()
    palindrome_set = set()
    for i in range(len(combined_str)):
        for j in range(i + 6, len(combined_str) + 1):
            candidate = combined_str[i:j]
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set