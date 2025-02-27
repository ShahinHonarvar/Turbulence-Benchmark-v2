def palindromes_of_specific_lengths(user_input):
    result = set()
    user_input = user_input.lower()
    for end in range(24, 63):
        for start in range(end - 21, end + 1):
            current = user_input[start:end + 1]
            if current == current[::-1] and 22 <= len(current) <= 33:
                result.add(current)
    return result