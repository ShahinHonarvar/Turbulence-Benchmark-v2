def palindrome_of_length_at_least_n(input_str):
    res = set()
    for i in range(len(input_str)):
        for j in range(i + 2, len(input_str) + 1):
            curr = input_str[i:j]
            if curr.lower() == curr[::-1].lower():
                res.add(curr)
    return res