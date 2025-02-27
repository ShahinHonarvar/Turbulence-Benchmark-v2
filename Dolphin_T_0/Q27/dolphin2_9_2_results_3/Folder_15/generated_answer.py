def insert_after_index(lst):
    return [v for i, v in enumerate(lst) for _ in [0, 1 if i == 0 else 0][:v]]