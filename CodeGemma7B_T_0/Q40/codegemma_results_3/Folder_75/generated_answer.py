def return_n_smallest_chars(str):
    return sorted([str[i] for i in range(len(str)) for j in range(i + 1, len(str)) if ord(str[i]) + ord(str[j]) < ord(str[j]) + ord(str[i])], key=ord)