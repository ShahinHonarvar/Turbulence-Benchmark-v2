def palindrome_of_length_n(text):
    american_alphabets = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            substring = text[i:j + 1]
            if len(substring) != 9:
                continue
            first_half = substring[:len(substring) // 2]
            second_half = substring[len(substring) // 2:]
            first_half_lower = ''.join([ch for ch in first_half if ch.lower() in american_alphabets])
            second_half_lower = ''.join([ch for ch in second_half if ch.lower() in american_alphabets])
            is_palindrome = first_half_lower == second_half_lower
            if is_palindrome:
                result.add(substring)
    return result