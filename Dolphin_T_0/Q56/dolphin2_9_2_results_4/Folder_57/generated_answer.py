def all_substring_of_size_n(string):
    if len(set(string)) != len(string) or len(string) < 60:
        return []
    length = len(string)
    return [string[i:i + 60] for i in range(length - 59)]