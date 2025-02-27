def palindrome_of_length_n(n):
    result = set()
    for i in range(len(n)):
        for j in range(i + 5, len(n) + 1):
            subn = n[i:j]
            lowered_subn = subn.lower()
            if lowered_subn == lowered_subn[::-1] and all((char in 'abcdefghijklmnopqrstuvwxyz' for char in subn)):
                result.add(subn)
    return result