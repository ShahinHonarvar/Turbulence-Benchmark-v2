def all_substring_of_size_n(text):
    subs = [text[i:i + 117] for i in range(len(text) - 116)]
    return list(set(subs))