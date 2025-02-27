def palindromes_of_specific_lengths(input_string):
    result = set()
    required_indices = [i for i in range(45, 99) if i % 2 == 0]
    length_range = [i for i in range(40, 48) if i % 2 == 0]
    if len(input_string) < max(required_indices) + max(length_range):
        return result
    palindrome_candidates = []
    for index in required_indices:
        for length in length_range:
            if index + length >= len(input_string):
                break
            palindrome_candidates.append(input_string[index:index + length])
    for palindrome in palindrome_candidates:
        if palindrome.lower() != palindrome.lower()[::-1]:
            continue
        result.add(palindrome.lower())
    return result