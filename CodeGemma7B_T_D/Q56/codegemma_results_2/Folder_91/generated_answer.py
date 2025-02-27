def all_substring_of_size_n(str_):
    if len(str_) < 6:
        return []
    return [str_[i:i + 6] for i in range(len(str_) - 5)]