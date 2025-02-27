def palindromes_of_specific_lengths(str):
    p = set()
    for i in range(101, 293):
        for j in range(i, 293):
            current = str[i:j + 1]
            current_lower = current.lower()
            if current_lower == current_lower[::-1] and len(current) >= 154 and (len(current) <= 182):
                p.add(current)
    return p